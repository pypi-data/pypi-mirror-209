#  See the NOTICE file distributed with this work for additional information
#  regarding copyright ownership.
#
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""Ensembl ValueSets client example."""

import grpc
from src.grpcapi.ensembl.valuesets.valuesets_pb2 import ValueSetRequest
from src.grpcapi.ensembl.valuesets.valuesets_pb2_grpc import ValueSetStub

from typer import Typer

client_app = Typer()


def init_client():
    channel = grpc.insecure_channel("localhost:50051")
    return ValueSetStub(channel)


@client_app.command()
def get_ok():
    client = init_client()
    request = ValueSetRequest(accession_id="mane.select")
    print(client.GetValueSetByAccessionId(request))


@client_app.command()
def get_ko():
    client = init_client()
    request = ValueSetRequest(accession_id="foobar")
    print(client.GetValueSetByAccessionId(request))


@client_app.command()
def get_vs_by_accession(accession_id: str):
    client = init_client()
    request = ValueSetRequest(accession_id=accession_id)
    print(client.GetValueSetByAccessionId(request))


@client_app.command()
def get_vs_by_value(value: str, is_current: bool = True):
    client = init_client()
    request = ValueSetRequest(value=value, is_current=is_current)
    vsets = client.GetValueSetsByValue(request).valuesets
    print(f"Returned {len(vsets)} ValueSets")
    for vv in vsets:
        print(f"{vv.accession_id} - {vv.is_current}")


@client_app.command()
def get_vs_by_domain(domain: str, is_current: bool = True):
    client = init_client()
    request = ValueSetRequest(accession_id=domain, is_current=is_current)
    vsets = client.GetValueSetsByDomain(request).valuesets
    print(f"Returned {len(vsets)} ValueSets")
    for vv in vsets:
        print(f"{vv.accession_id} - {vv.is_current}")


if __name__ == "__main__":
    client_app()
