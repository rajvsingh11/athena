from app.schemas.health import HealthResponse

def get_health_status() -> HealthResponse:
    return HealthResponse(
        status="healthy",
        service="athena-api",
        version="0.1.0"
    )