"use strict";

const announce = (message) => {
  const status = document.getElementById("status");
  if (status) status.textContent = message;
};

for (const block of document.querySelectorAll("pre")) {
  const code = block.querySelector("code");
  if (!code || !navigator.clipboard) continue;
  const button = document.createElement("button");
  button.type = "button";
  button.className = "copy";
  button.textContent = "Copy code";
  button.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(code.textContent);
      announce("Code copied. Review and adapt project-specific commands before running.");
    } catch (error) {
      console.warn("Clipboard access failed:", error);
      announce("Clipboard unavailable. Select the code and copy it manually.");
    }
  });
  block.before(button);
}

const panel = document.querySelector(".progress-panel");
if (panel) {
  panel.classList.add("active");
  const key = "embedded-workshop-progress-v1";
  const page = document.body.dataset.lab;
  const button = document.getElementById("complete");
  try {
    const stored = JSON.parse(localStorage.getItem(key) || "[]");
    if (!Array.isArray(stored) || stored.some((entry) => typeof entry !== "string")) {
      throw new TypeError("Unexpected progress storage format");
    }
    const complete = new Set(stored);
    button.textContent = complete.has(page) ? "Mark as not completed" : "Mark this lab completed";
    button.addEventListener("click", () => {
      if (complete.has(page)) complete.delete(page);
      else complete.add(page);
      try {
        localStorage.setItem(key, JSON.stringify([...complete]));
        button.textContent = complete.has(page) ? "Mark as not completed" : "Mark this lab completed";
        announce("Progress saved in this browser only. Optional modules are not required for completion.");
      } catch (error) {
        console.warn("Progress could not be saved:", error);
        button.disabled = true;
        announce("Progress storage unavailable. All workshop content remains accessible.");
      }
    });
  } catch (error) {
    console.warn("Progress storage could not be read:", error);
    button.disabled = true;
    announce("Progress storage unavailable. All workshop content remains accessible.");
  }
}
