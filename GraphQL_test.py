from fastapi.testclient import TestClient
from GraphQL import app

client = TestClient(app)

def test_users():
        query = """
        query {
            users {
                id
                name
                email
            }
        }
        """
        response = client.post("/graphql" , json={"query": query})
        assert response.status_code == 200
        response_data = response.json()
        assert "data" in response_data


def test_mutation_add_user():
    mutation = """
        mutation { 
            addUser(name: "Kurt Cobain", email: "nirvana@gmail.com") {
                id
                name
                email
            }
        }
        """

    response = client.post("/graphql", json={"query": mutation})
    assert response.status_code == 200
    result = response.json()["data"]["addUser"]
    assert result["name"] == "Kurt Cobain"
    assert result["email"] == ("nirvana@gmail.com")