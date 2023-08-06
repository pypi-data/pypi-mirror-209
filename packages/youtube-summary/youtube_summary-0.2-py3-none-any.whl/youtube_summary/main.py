from typing import List
from urllib.parse import parse_qs, urlparse

import typer
from langchain import LLMChain, PromptTemplate
from langchain.callbacks import get_openai_callback
from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from youtube_transcript_api import NoTranscriptFound, YouTubeTranscriptApi
import re
from collections import namedtuple
from rich.console import Console


# Define named tuple
SectionSummary = namedtuple("SectionSummary", ["timestamp_seconds", "text"])

app = typer.Typer()

SECTION_TITLES_PROMPT = """Your mission is to summarize a video using its subtitles.
The subtitles will be given between the triple backticks (```). The format of the subtitles will be ` [timestamp in seconds]: [text]`. 
For each sentence in the summary, you should provide the start time of the video section that this sentence is based on.
For example, a summary of a video section that starts in second 31 will be: `[31]: section summary`
Here are the subtitles:
```
{text}
```
Your summary:
"""
SECTION_TITLES_PROMPT_TEMPLATE = PromptTemplate(
    template=SECTION_TITLES_PROMPT, input_variables=["text"]
)

SUMMARY_PROMPT = """Your mission is to write a conscise summary of a video using its section summaries.
The section summaries will be given between the triple backticks (```). The format of the section summaries will be ` [timestamp in seconds]: [summary]`.
Here are the section summaries:
```
{text}
```
Your concise video summary:"""
SUMMARY_PROMPT_TEMPLATE = PromptTemplate(
    template=SUMMARY_PROMPT, input_variables=["text"]
)


class InvalidURLException(Exception):
    pass


def get_videoid_from_url(url: str) -> str:
    """
    Gets video ID from give YouTube video URL

    :param url: YouTube video URL in 2 formats (standard and short)
    :return: id of YouTube video
    :raises InvalidURLException: If URL is not valid
    """
    url_data = urlparse(url)
    query = parse_qs(url_data.query)

    if ("v" in query) & ("youtube.com" in url_data.netloc):
        video_id = query["v"][0]
    elif "youtu.be" in url_data.netloc:
        path_lst = url.split("/")

        if path_lst:
            video_id = path_lst[-1]
        else:
            raise InvalidURLException("Invalid URL")
    else:
        raise InvalidURLException("Invalid URL")

    return video_id


def get_transcripts(url: str) -> str:
    video_id = get_videoid_from_url(url)

    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    try:
        transcript = transcript_list.find_manually_created_transcript(["en"])
    except NoTranscriptFound:
        transcript = transcript_list.find_generated_transcript(["en"])

    subtitles = transcript.fetch()

    subtitles = "\n".join(
        [
            f"{sbt['start']}: {sbt['text']}"
            for sbt in subtitles
            if sbt["text"] != "[Music]"
        ]
    )

    return subtitles


def generate_section_summaries(subtitles: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n"], chunk_size=2048, chunk_overlap=200
    )
    docs = text_splitter.create_documents([subtitles])

    map_chain = LLMChain(llm=llm, prompt=SECTION_TITLES_PROMPT_TEMPLATE, verbose=False)
    reduce_chain = LLMChain(
        llm=llm, prompt=SECTION_TITLES_PROMPT_TEMPLATE, verbose=False
    )
    combine_document_chain = StuffDocumentsChain(
        llm_chain=reduce_chain,
        document_variable_name="text",
        verbose=False,
    )
    map_reduce_chain = MapReduceDocumentsChain(
        llm_chain=map_chain,
        combine_document_chain=combine_document_chain,
        document_variable_name="text",
        verbose=False,
    )
    result = map_reduce_chain(docs)
    return result["output_text"]


def generate_summary(section_titles: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    document = Document(page_content=section_titles)
    chain = LLMChain(llm=llm, prompt=SUMMARY_PROMPT_TEMPLATE, verbose=False)
    result = chain([document])
    return result["text"]


def parse_section_summaries_text(text: str) -> List[SectionSummary]:
    # Split text into lines
    lines = text.split("\n")

    parsed_lines = []

    # Parse each line
    for line in lines:
        match = re.match(r"\s*\[(\d+(?:\.\d+)?)\]:\s+(.*)", line)
        if match:
            timestamp_seconds, text = match.groups()
            parsed_line = SectionSummary(
                timestamp_seconds=int(float(timestamp_seconds)), text=text
            )
            parsed_lines.append(parsed_line)

    return parsed_lines


def get_pretty_section_summary_text(url: str, section_summaries: str) -> str:
    parsed_section_summaries = parse_section_summaries_text(section_summaries)
    pretty_summaries = []
    for section_summary in parsed_section_summaries:
        timestamp_seconds = section_summary.timestamp_seconds
        link = f"{url}&t={timestamp_seconds}"
        timestamp_pretty = f"{timestamp_seconds // 3600}:{timestamp_seconds // 60}:{timestamp_seconds % 60}"
        summary = f"[link={link}]{timestamp_pretty}[/link]: {section_summary.text}"
        pretty_summaries.append(summary)
    return "\n".join(pretty_summaries)


@app.command()
def main(url: str):
    console = Console(highlight=False)

    subtitles = get_transcripts(url)

    with get_openai_callback() as cb:
        section_summaries = generate_section_summaries(subtitles)
        summary = generate_summary(section_summaries)

    console.print()
    console.print("[bold]Summary:[/bold]")
    console.print(summary)

    console.print()
    console.print("[bold]Section summaries:[/bold]")
    console.print(get_pretty_section_summary_text(url, section_summaries))

    console.print()
    console.print("[bold]OpenAI Stats:[/bold]")
    console.print(cb)
