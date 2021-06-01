import pytest
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from tests.conftest import api_client, course_factory, student_factory


# def test_example():
#     assert False, "Just test example"


@pytest.mark.django_db
def test_course_retrieve(api_client, course_factory):
    course = course_factory(name='Python')
    assert course.id
    url = reverse('courses-detail', args=(course.id,))
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json['name'] == 'Python'


@pytest.mark.django_db
def test_course_list(api_client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse('courses-list')
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 3


@pytest.mark.django_db
def test_course_by_id(api_client, course_factory):
    courses = course_factory(_quantity=3)
    course = course_factory(id=10)
    url = reverse('courses-list') + '?id=10'
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_first = resp.json()[0]
    assert resp_first['id'] == 10


@pytest.mark.django_db
def test_course_by_name(api_client, course_factory):
    courses = course_factory(_quantity=3)
    course = course_factory(name='Python')
    url = reverse('courses-list') + '?name=Python'
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_first = resp.json()[0]
    assert resp_first['name'] == 'Python'


@pytest.mark.django_db
def test_add_course(api_client):
    url = reverse('courses-list')
    course_payload = {
        'name': 'Python'
    }
    resp = api_client.post(url, course_payload)
    assert resp.status_code == HTTP_201_CREATED


@pytest.mark.django_db
def test_course_update(api_client, course_factory):
    course = course_factory(name='Python')
    assert course.id
    url = reverse('courses-detail', args=(course.id,))
    course_payload = {
        'name': 'Kotlin'
    }
    resp = api_client.patch(url, course_payload)
    assert resp.status_code == HTTP_200_OK
    assert resp.json()['name'] == 'Kotlin'



@pytest.mark.django_db
def test_course_update(api_client, course_factory):
    course = course_factory(name='Python')
    assert course.id
    url = reverse('courses-detail', args=(course.id,))
    resp = api_client.delete(url)
    assert resp.status_code == HTTP_204_NO_CONTENT
