import logging
from fastapi import APIRouter, HTTPException
from app.db.mongodb import create_challenge, get_challenge, create_solution, get_solution
from app.schemas.persistence import PersistedChallenge, PersistedSolution
logger = logging.getLogger(__name__)
router = APIRouter(prefix='/api', tags=['persistence'])

@router.post('/challenges', status_code=201)
def save_challenge(challenge: PersistedChallenge):
    try: return {'status':'success','challenge_id':create_challenge(challenge.model_dump()),'message':'Challenge saved successfully'}
    except Exception:
        logger.exception('Challenge persistence failed')
        raise HTTPException(503, 'Unable to save the challenge right now.')

@router.get('/challenges/{challenge_id}')
def read_challenge(challenge_id: str):
    try: document = get_challenge(challenge_id)
    except Exception: document = None
    if not document: raise HTTPException(404, 'Challenge not found.')
    return {'status':'success','challenge':document}

@router.post('/solutions', status_code=201)
def save_solution(solution: PersistedSolution):
    try: return {'status':'success','solution_id':create_solution(solution.model_dump()),'message':'Solution saved successfully'}
    except Exception:
        logger.exception('Solution persistence failed')
        raise HTTPException(503, 'Unable to save the solution right now.')

@router.get('/solutions/{solution_id}')
def read_solution(solution_id: str):
    try: document = get_solution(solution_id)
    except Exception: document = None
    if not document: raise HTTPException(404, 'Solution not found.')
    return {'status':'success','solution':document}
