document.getElementById("loginForm").addEventListener("submit", async function(event) {
  event.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const response = await fetch("http://localhost:8000/login_ames", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });

    if (!response.ok) {
      const errorResult = await response.json();
      const errorMsg = errorResult.detail || "Login failed";
      document.getElementById("message").textContent = errorMsg;
      return;
    }

    const result = await response.json();
    const username = result.username || result.user || "User";

    document.getElementById("message").textContent = "";
    window.location.href = `events.html?username=${encodeURIComponent(username)}`;
  } catch (error) {
    document.getElementById("message").textContent = "Error connecting to server";
  }
});
