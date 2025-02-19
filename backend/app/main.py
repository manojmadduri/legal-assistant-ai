from fastapi import FastAPI
from .routes import contracts, compliance, ip_filing, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS setup
origins = ["*"]  # For development, allow all. Restrict in production.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(contracts.router, prefix="/contracts", tags=["Contracts"])
app.include_router(compliance.router, prefix="/compliance", tags=["Compliance"])
app.include_router(ip_filing.router, prefix="/ip-filing", tags=["IP Filing"])

@app.get("/")
def root():
    return {"message": "AI Legal Assistant API is running"}
