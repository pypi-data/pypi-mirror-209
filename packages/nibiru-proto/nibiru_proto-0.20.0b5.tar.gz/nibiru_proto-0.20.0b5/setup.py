# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nibiru_proto',
 'nibiru_proto.proto',
 'nibiru_proto.proto.confio',
 'nibiru_proto.proto.cosmos.auth.v1beta1',
 'nibiru_proto.proto.cosmos.authz.v1beta1',
 'nibiru_proto.proto.cosmos.bank.v1beta1',
 'nibiru_proto.proto.cosmos.base.abci.v1beta1',
 'nibiru_proto.proto.cosmos.base.kv.v1beta1',
 'nibiru_proto.proto.cosmos.base.node.v1beta1',
 'nibiru_proto.proto.cosmos.base.query.v1beta1',
 'nibiru_proto.proto.cosmos.base.reflection.v1beta1',
 'nibiru_proto.proto.cosmos.base.reflection.v2alpha1',
 'nibiru_proto.proto.cosmos.base.snapshots.v1beta1',
 'nibiru_proto.proto.cosmos.base.store.v1beta1',
 'nibiru_proto.proto.cosmos.base.tendermint.v1beta1',
 'nibiru_proto.proto.cosmos.base.v1beta1',
 'nibiru_proto.proto.cosmos.capability.v1beta1',
 'nibiru_proto.proto.cosmos.crisis.v1beta1',
 'nibiru_proto.proto.cosmos.crypto.ed25519',
 'nibiru_proto.proto.cosmos.crypto.multisig',
 'nibiru_proto.proto.cosmos.crypto.multisig.v1beta1',
 'nibiru_proto.proto.cosmos.crypto.secp256k1',
 'nibiru_proto.proto.cosmos.crypto.secp256r1',
 'nibiru_proto.proto.cosmos.distribution.v1beta1',
 'nibiru_proto.proto.cosmos.evidence.v1beta1',
 'nibiru_proto.proto.cosmos.feegrant.v1beta1',
 'nibiru_proto.proto.cosmos.genutil.v1beta1',
 'nibiru_proto.proto.cosmos.gov.v1beta1',
 'nibiru_proto.proto.cosmos.mint.v1beta1',
 'nibiru_proto.proto.cosmos.params.v1beta1',
 'nibiru_proto.proto.cosmos.slashing.v1beta1',
 'nibiru_proto.proto.cosmos.staking.v1beta1',
 'nibiru_proto.proto.cosmos.tx.signing.v1beta1',
 'nibiru_proto.proto.cosmos.tx.v1beta1',
 'nibiru_proto.proto.cosmos.upgrade.v1beta1',
 'nibiru_proto.proto.cosmos.vesting.v1beta1',
 'nibiru_proto.proto.cosmos_proto',
 'nibiru_proto.proto.epochs.v1',
 'nibiru_proto.proto.gogoproto',
 'nibiru_proto.proto.google.api',
 'nibiru_proto.proto.google.protobuf',
 'nibiru_proto.proto.inflation.v1',
 'nibiru_proto.proto.oracle.v1',
 'nibiru_proto.proto.perp.v2',
 'nibiru_proto.proto.spot.v1',
 'nibiru_proto.proto.stablecoin.v1',
 'nibiru_proto.proto.sudo.v1',
 'nibiru_proto.proto.tendermint.abci',
 'nibiru_proto.proto.tendermint.crypto',
 'nibiru_proto.proto.tendermint.libs.bits',
 'nibiru_proto.proto.tendermint.p2p',
 'nibiru_proto.proto.tendermint.types',
 'nibiru_proto.proto.tendermint.version']

package_data = \
{'': ['*']}

install_requires = \
['asyncio>=3.4.3,<4.0.0',
 'bech32>=1.2.0,<2.0.0',
 'grpcio-tools>=1.51.1,<2.0.0',
 'grpcio>=1.51.1,<2.0.0',
 'mypy-protobuf>=3.4.0,<4.0.0',
 'protobuf>=4.21.12,<5.0.0',
 'types-protobuf>=4.21.0.2,<5.0.0.0']

setup_kwargs = {
    'name': 'nibiru-proto',
    'version': '0.20.0b5',
    'description': 'Nibiru Chain Python SDK',
    'long_description': 'None',
    'author': 'Nibiru Chain',
    'author_email': 'dev@nibiru.fi',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
