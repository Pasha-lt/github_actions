import requests

def test_ghimbli():
    response = requests.request('GET', 'https://ghibliapi.vercel.app/films')

    assert response.status_code == 200

def test_T():
    assert True