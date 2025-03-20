from azure_openai import *
from pprint import pprint
import traceback
import json
from azure_blob.azure_blob_helper import AzureBlobHelper

from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import *
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

verbose = True
search_creds = AzureKeyCredential(searchkey)

from config_openai import *

context = """
The men's high jump event at the 2020 Summer Olympics took place between 30 July and 1 August 2021 at the Olympic Stadium.
33 athletes from 24 nations competed; the total possible number depended on how many nations would use universality places
to enter athletes in addition to the 32 qualifying through mark or ranking (no universality places were used in 2021).
Italian athlete Gianmarco Tamberi along with Qatari athlete Mutaz Essa Barshim emerged as joint winners of the event following
a tie between both of them as they cleared 2.37m. Both Tamberi and Barshim agreed to share the gold medal in a rare instance
where the athletes of different nations had agreed to share the same medal in the history of Olympics.
Barshim in particular was heard to ask a competition official "Can we have two golds?" in response to being offered a
'jump off'. Maksim Nedasekau of Belarus took bronze. The medals were the first ever in the men's high jump for Italy and
Belarus, the first gold in the men's high jump for Italy and Qatar, and the third consecutive medal in the men's high jump
for Qatar (all by Barshim). Barshim became only the second man to earn three medals in high jump, joining Patrik Sjöberg
of Sweden (1984 to 1992)."""

query = "Who won the gold in high jump event at the 2020 Summer Olympics?"


def get_reply():
    try:
        answer = generate_reply_from_context(query, context,[])
        return answer
    except Exception as e:
        pprint(e.__str__())
        return(f"Error in get_reply - {e.__str__()}")

def get_search_indexes_helper():
    try:
        verbose = True
        search_creds = AzureKeyCredential(searchkey)

        index_client = SearchIndexClient(endpoint=f"https://{searchservice}.search.windows.net/",
                                        credential=search_creds)
                
        return [index for index in index_client.list_index_names()]
    except Exception as e:
        pprint(e.__str__())
        return(f"Error in get_search_indexes_helper - {e.__str__()}")

def get_blobs_helper():
    azure_blob_helper = AzureBlobHelper(AZ_ST_ACC_NAME,
                                    AZ_ST_ACC_KEY,
                                    AZ_ST_CONTAINER_NAME)
    return(azure_blob_helper.list_blob())