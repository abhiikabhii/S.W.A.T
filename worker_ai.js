export default {
  async fetch(request) {
    // Mock inference that checks if any parameter is near unsafe threshold
    const data = await request.json();

    let risk = 0;
    if (data.ph < 6.5 || data.ph > 8.5) risk += 30;
    if (data.turbidity > 5) risk += 40;
    if (data.flow < 0.2) risk += 50;

    return new Response(JSON.stringify({
      ai_risk_score: Math.min(risk, 100),
      message: "Edge inference complete"
    }), { headers: { "Content-Type": "application/json" }});
  }
};
