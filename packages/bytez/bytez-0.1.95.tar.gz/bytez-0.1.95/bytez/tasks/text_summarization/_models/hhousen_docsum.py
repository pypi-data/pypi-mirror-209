from typing import BinaryIO
from bytez.model import Model


class HhousenDocsumModel(Model):
    def inference(self, input_pdf: BinaryIO, preprocess: bool = True, model: str = 'bart', bart_checkpoint: str = None, bart_state_dict_key: str = 'model', bart_fairseq: bool = False, chapter_heading_font: int = 0, body_heading_font: int = 3, body_font: int = 1) -> bytes:
        """
        Runs text summarization on a given PDF file and returns the output as a dictionary of chapter and headings to summarized text.

Args:

- input_pdf (BinaryIO): The binary PDF file to be summarized.
- preprocess (bool, optional): Whether to preprocess the PDF file before summarization. Defaults to True.
- model (str, optional): The summarization model to use. Must be either 'bart' or 'presumm'. Defaults to 'bart'.
- bart_checkpoint (str, optional): Path to the optional BART checkpoint file. Semsim is better model but will use more memory and is an additional 5GB download. Defaults to None.
- bart_state_dict_key (str, optional): The state_dict key to load from pickle file specified with `bart_checkpoint`. Defaults to 'model'.
- bart_fairseq (bool, optional): Use fairseq model from torch hub instead of huggingface transformers library models. Can not use `bart_checkpoint` if this option is supplied. Defaults to False.
- chapter_heading_font (int, optional): The font of the chapter titles. Defaults to 0.
- body_heading_font (int, optional): The font of headings within chapter. Defaults to 3.
- body_font (int, optional): The font of the body (the text you want to summarize). Defaults to 1.

Returns:

- Dict[str, str]: The output of the summarization. This is a dictionary of chapter and headings to summarized text.
        """

        request_params = {
    "input_pdf": input_pdf,
    "preprocess": preprocess,
    "model": model,
    "bart_checkpoint": bart_checkpoint,
    "bart_state_dict_key": bart_state_dict_key,
    "bart_fairseq": bart_fairseq,
    "chapter_heading_font": chapter_heading_font,
    "body_heading_font": body_heading_font,
    "body_font": body_font
}

        url = 'https://hhousen-docsum-tfhmsoxnpq-uc.a.run.app'

        return self._Model__inference(url=url, request_params=request_params)