#from tasks.ner import NamedEntityRecognition
from .ner import NamedEntityRecognition


DESCRIPTION = """

emi-manually defined in this case as: Bootstrapped from Swedish Gazetters then manually correcte/reviewed by two independent native speaking swedish annotators

"""


_CITATION = """


"""


class SwedishNer(NamedEntityRecognition):

    """
    Class for Swedish NER
    """
    
    DATASET_ID = "swedish_ner_corpus"  # HF datasets ID
    TASK_NAME = "swedish_ner"
    HOMEPAGE_URL = "https://huggingface.co/datasets/swedish_ner_corpus"
    LABEL_NAME = "ner_tags"

    def get_dataset_id(self):
        return self.DATASET_ID

    def get_task_name(self):
        return self.TASK_NAME

    def get_url(self):
        return self.HOMEPAGE_URL
    
    def get_label_name(self):
        return self.LABEL_NAME
