from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.modules.dashboard.schema import DashboardSummaryResponse
from src.modules.dashboard.service import get_dashboard_summary

from src.core.db.session import get_db


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary", response_model=DashboardSummaryResponse)
def dashboard_summary(
    db: Session = Depends(get_db)
):
    """
    Returns dashboard summary analytics
    """

    return get_dashboard_summary(db)
