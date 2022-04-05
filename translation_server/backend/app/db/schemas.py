from pydantic import BaseModel, parse_obj_as
from typing import Optional, TypedDict, Dict, List

class NewUser(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TMXData(BaseModel):
    src: str
    target: str
    tuid: str

class TokenData(BaseModel):
    username: Optional[str] = None

# [{"src_sent": "My sentence 1."}, {"src_sent":"My sentence 2."}, {"src_sent":"My sentence 3."}]
class QuerData(BaseModel):
    src_sent: str

class TranslationDataRequest(BaseModel):
    __root__: List[QuerData]

    # req_query: List[query_data]

# [{"src_sent": "My sentence 1.", "tgt_sent": "Mein Satz 1."}, 
# {"src_sent": "My sentence 2.", "tgt_sent": "Mein Satz 2."}, 
# {"src_sent": "My sentence 3.", "tgt_sent": "Mein Satz 3."}]
class res_atom(BaseModel):
    src_sent: str
    tgt_sent: str

class TranslationDataResponse(BaseModel):
    res_data: List[res_atom]
    