from ckanext.downloadall import helpers


def test_pop_zip_resource_does_not_mutate_empty_package():
    package = {}

    assert helpers.pop_zip_resource(package) is None
    assert package == {}


def test_pop_zip_resource_removes_and_returns_zip_resource():
    regular_resource = {'id': 'regular-resource'}
    zip_resource = {
        'id': 'zip-resource',
        'downloadall_metadata_modified': '2026-09-29T05:36:04',
    }
    package = {'resources': [regular_resource, zip_resource]}

    assert helpers.pop_zip_resource(package) == zip_resource
    assert package['resources'] == [regular_resource]
