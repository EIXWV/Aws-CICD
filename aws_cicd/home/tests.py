from django.test import TestCase
from django import urls
import pytest

def test_exaple():
    assert 1 == 1 

@pytest.mark.parametrize('param',[('home'),('index')])
def test_render_views(client,param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200

# Create your tests here.
