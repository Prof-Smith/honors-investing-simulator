<script lang="ts">
    import { goto } from '$app/navigation';

    type Option = {
        label: string;
        score: number;
    };

    type Question = {
        id: number;
        text: string;
        options: Option[];
    };

    const questions: Question[] = [
        {
            id: 1,
            text: "If your portfolio fell 25% in a single year, what would you do?",
            options: [
                { label: "Sell everything immediately", score: 0 },
                { label: "Sell some investments", score: 30 },
                { label: "Do nothing and wait", score: 65 },
                { label: "Buy more at lower prices", score: 100 }
            ]
        },
        {
            id: 2,
            text: "Which outcome would bother you more?",
            options: [
                { label: "Losing 10% in a bad year", score: 20 },
                { label: "Missing out on large gains", score: 80 }
            ]
        },
        {
            id: 3,
            text: "Your primary investment horizon is:",
            options: [
                { label: "Less than 3 years", score: 10 },
                { label: "3–10 years", score: 40 },
                { label: "10–25 years", score: 75 },
                { label: "25+ years", score: 100 }
            ]
        },
        {
            id: 4,
            text: "How do you react to volatile markets?",
            options: [
                { label: "I closely monitor and feel stressed", score: 15 },
                { label: "I’m uncomfortable but stay invested", score: 45 },
                { label: "I ignore short‑term noise", score: 75 },
                { label: "I look for buying opportunities", score: 100 }
            ]
        },
        {
            id: 5,
            text: "Which portfolio do you prefer?",
            options: [
                { label: "Stable with low growth", score: 20 },
                { label: "Balanced growth and stability", score: 55 },
                { label: "High growth with large swings", score: 100 }
            ]
        }
    ];

    let answers: Record<number, number> = {};

    function computeRisk() {
        const values = Object.values(answers);
        const avg = values.reduce((a, b) => a + b, 0) / values.length;
        const riskScore = Math.round(avg);

        sessionStorage.setItem('riskScore', String(riskScore));
        goto('/allocation');
    }
</script>

<h1>Risk Tolerance Questionnaire</h1>
<p class="subtitle">
    There are no correct answers. Choose what best reflects <em>your behavior</em>.
</p>

<form class="questionnaire">
    {#each questions as q}
        <fieldset>
            <legend>{q.text}</legend>

            {#each q.options as opt}
                <label>
                    <input
                        type="radio"
                        name={"q" + q.id}
                        on:change={() => (answers[q.id] = opt.score)}
                    />
                    <span>{opt.label}</span>
                </label>
            {/each}
        </fieldset>
    {/each}

    <button
        type="button"
        disabled={Object.keys(answers).length !== questions.length}
        on:click={computeRisk}
    >
        Continue →
    </button>
</form>

<style>
    h1 {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }

    .subtitle {
        color: #555;
        margin-bottom: 2rem;
    }

    fieldset {
        border: none;
        margin-bottom: 2rem;
    }

    legend {
        font-weight: 600;
        margin-bottom: 0.75rem;
    }

    label {
        display: block;
        margin-bottom: 0.5rem;
        cursor: pointer;
    }

    input[type="radio"] {
        margin-right: 0.5rem;
    }

    button {
        margin-top: 1.5rem;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        border: none;
        border-radius: 6px;
        background: #2563eb;
        color: white;
        cursor: pointer;
    }

    button:disabled {
        background: #bbb;
        cursor: not-allowed;
    }
</style>