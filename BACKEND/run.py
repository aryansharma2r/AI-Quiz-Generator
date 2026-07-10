# run.py
# This file is the entry point to start the FastAPI application
# using the uvicorn server.

import uvicorn

# Standard Python entry point
# This block runs only when this file is executed directly
# (not when it is imported elsewhere)
if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",   # path to the FastAPI app instance (module:variable)
        host="127.0.0.1", # run locally on this host
        port=8000,        # port number to run the server on
        reload=True       # auto-restart server when code changes (useful in development)
    )