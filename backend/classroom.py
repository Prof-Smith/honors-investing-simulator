class Classroom:
    def __init__(self):
        self.records = []

    def submit(self, record: dict):
        self.records.append(record)

    def summary(self):
        if not self.records:
            return {
                "avg_risk": 0,
                "avg_stock": 0,
                "failure_rates": []
            }

        avg_risk = sum(r["risk"] for r in self.records) / len(self.records)
        avg_stock = sum(r["stock"] for r in self.records) / len(self.records)
        failure_rates = [r["failure"] for r in self.records]

        return {
            "avg_risk": round(avg_risk, 2),
            "avg_stock": round(avg_stock, 2),
            "failure_rates": failure_rates
        }


CLASSROOM = Classroom()
