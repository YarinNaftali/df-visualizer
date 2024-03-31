import pytest
from httpx import AsyncClient, ASGITransport

from main import app


@pytest.mark.anyio
async def test_root():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test/api/v1/files"
    ) as ac:
        response = await ac.get("/all-files")
    assert response.status_code == 200
    assert response.json() == []
