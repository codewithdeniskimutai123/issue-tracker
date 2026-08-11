from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

@router.get("/issues")
def get_issues():
    return []