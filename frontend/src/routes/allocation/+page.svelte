<script lang="ts">
    import { goto } from '$app/navigation';

    const riskScore = Number(sessionStorage.getItem('riskScore'));

    if (Number.isNaN(riskScore)) {
        goto('/risk');
    }

    function allocationFromRisk(score: number) {
        if (score <= 20) return { stocks: 20, bonds: 80 };
        if (score <= 40) return { stocks: 40, bonds: 60 };
        if (score <= 60) return { stocks: 60, bonds: 40 };
        if (score <= 80) return { stocks: 80, bonds: 20 };
        return { stocks: 95, bonds: 5 };
    }

    const allocation = allocationFromRisk(riskScore);
</script>

<h1>Your Implied Portfolio Allocation</h1>

<p class="subtitle">
    Based on your risk tolerance score of
    <strong>{riskScore}</strong>,
    a simple long‑term portfolio might look like:
</p>

<div class="allocation">
    <div class="bar stocks" style="width: {allocation.stocks}%">
        Stocks {allocation.stocks}%
    </div>
    <div class="bar bonds" style="width: {allocation.bonds}%">
        Bonds {allocation.bonds}%
    </div>
</div>

<p class="explanation">
    Higher stock allocations increase long‑term expected growth,
    but also increase short‑term volatility.
</p>

<button on:click={() => goto('/simulation')}>
    See What This Means Over Time →
</button>

<style>
    h1 {
        font-size: 2rem;
        margin-bottom: 0.75rem;
    }

    .subtitle {
        color: #555;
        margin-bottom: 2rem;
    }

    .allocation {
        width: 100%;
        margin: 2rem 0;
        border-radius: 6px;
        overflow: hidden;
        display: flex;
        background: #eee;
    }

    .bar {
        padding: 1rem;
        color: white;
        font-weight: 600;
        text-align: center;
    }

    .stocks {
        background: #16a34a;
    }

    .bonds {
        background: #0284c7;
    }

    .explanation {
        margin-top: 1.5rem;
        color: #444;
    }

    button {
        margin-top: 2rem;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        border-radius: 6px;
        border: none;
        background: #2563eb;
        color: white;
        cursor: pointer;
    }
</style>
