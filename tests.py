from aws_fuzzy_finder.aws_utils import prepare_searchable_instances


class TestInstanceView:
    example_reservations = [{
        u'Groups': [],
        u'Instances': [{
            u'PrivateIpAddress': '10.121.111.123',
            u'State': {
                u'Code': 16,
                u'Name': 'running'
            },
            u'Tags': [{
                u'Key': 'Name',
                u'Value': 'test_foobar"'
            }],
            u'VpcId': 'vpc-f2ccsd34f'
        }, {
            u'PrivateIpAddress': '10.121.12.34',
            u'State': {
                u'Code': 16,
                u'Name': 'running'
            },
            u'Tags': [{
                u'Key': 'Name',
                u'Value': 'prod_something'
            }],
            u'VpcId': 'vpc-2342sfd2'
        }, {
            u'PrivateIpAddress': '10.121.12.55',
            u'PublicIpAddress': '52.123.12.32',
            u'State': {
                u'Code': 16,
                u'Name': 'running'
            },
            u'Tags': [{
                u'Key': 'Name',
                u'Value': 'prod_something2'
            }],
            u'VpcId': 'vpc-2342sfd2'
        }]
    }]

    def test_getting_private_ip(self):
        searchable_instances = prepare_searchable_instances(
            reservations=self.example_reservations,
            use_private_ip=True
        )
        assert searchable_instances == [
            'test_foobar @ 10.121.111.123',
            'prod_something @ 10.121.12.34',
            'prod_something2 @ 10.121.12.55',
        ]

    def test_getting_public_ip(self):
        searchable_instances = prepare_searchable_instances(
            reservations=self.example_reservations,
            use_private_ip=False
        )
        assert searchable_instances == [
            'test_foobar @ 10.121.111.123',
            'prod_something @ 10.121.12.34',
            'prod_something2 @ 52.123.12.32',
        ]
