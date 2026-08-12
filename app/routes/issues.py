import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueUpdate, IssueOut, IssueStatus, IssuePriority
from app.storage import save_issues, load_issues

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

@router.get("/issues", response_model=list[IssueOut])
def get_issues():
    """Retrieve all issues."""
    issues = load_issues()
    return issues

@router.post("/issues", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
def create_issue(payload: IssueCreate) -> IssueOut:
    """Create a new issue."""
    issues = load_issues()
    new_issue = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.description,
        "status": IssueStatus.open.value,
        "priority": payload.priority.value
    }
    issues.append(new_issue)
    save_issues(issues)
    return new_issue

@router.get("/issues/{issue_id}", response_model=IssueOut)
def get_issue(issue_id: str) -> IssueOut:
    """Retrieve a specific issue by ID."""
    issues = load_issues()
    for issue in issues:
        if issue["id"] == issue_id:
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.put("/issues/{issue_id}", response_model=IssueOut)
def update_issue(issue_id: str, payload: IssueUpdate) -> IssueOut:
    """Update an existing issue."""
    issues = load_issues()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            updated_issue = issue.copy()
            if payload.title is not None:
                updated_issue["title"] = payload.title
            if payload.description is not None:
                updated_issue["description"] = payload.description
            if payload.status is not None:
                updated_issue["status"] = payload.status.value
            if payload.priority is not None:
                updated_issue["priority"] = payload.priority.value
            issues[index] = updated_issue
            save_issues(issues)
            return updated_issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.delete("/issues/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id: str):
    issues = load_issues()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            issues.pop(index)
            save_issues(issues)
            return 
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)