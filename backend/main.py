from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

from monte_carlo import accumulate, decumulate
from classroom import CLASSROOM

app = FastAPI()


class AccumInput(BaseModel):
    years: int
    contrib: float
    stock: float
    bond: float


@app.post("/accumulate")
def run_accumulation(p: AccumInput):
    paths = accumulate(
        p.years, p.contrib, p.stock, p.bond
    )

    return {
        "fan": np.percentile(paths, [10, 25, 50, 75, 90], axis=0).tolist(),
        "paths": paths[::10].tolist()
    }


class RetireInput(BaseModel):
    start: float
    years: int
    withdrawal: float
    stock: float
    bond: float
    risk: float


@app.post("/retire")
def run_retirement(p: RetireInput):
    paths, failure = decumulate(
        p.start, p.years, p.withdrawal, p.stock, p.bond
    )

    CLASSROOM.submit({
        "risk": p.risk,
        "stock": p.stock,
        "failure": failure
    })

    return {
        "fan": np.percentile(paths, [10, 25, 50, 75, 90], axis=0).tolist(),
        "failure": failure
    }


@app.get("/classroom")
def classroom_summary():
    return CLASSROOM.summary()
