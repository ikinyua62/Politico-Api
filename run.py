from app create_app
from app.api.V1.view.partyview import Party

app=create_app()



if __name__ == "__main__":
    app.run(debug=True)

