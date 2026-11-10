"use strict";
/* Public, read-only GitHub Pages viewer. No GitHub API token is used. */
(function () {
  var categories = [
    { name: "session1", list: "student-list-1", count: "count-1" },
    { name: "session2", list: "student-list-2", count: "count-2" },
    { name: "etc", list: "student-list-etc", count: "count-etc" }
  ];
  function empty(list, msg) {
    var li = document.createElement("li");
    li.className = "empty";
    li.textContent = msg;
    list.replaceChildren(li);
  }
  function safeUrl(row, section, base) {
    if (!row || typeof row.name !== "string" || !row.name.trim()) return null;
    try {
      if (row.type === "link" && section === "etc" && typeof row.url === "string") {
        var link = new URL(row.url);
        if ((link.protocol === "https:" || link.protocol === "http:") && link.hostname && !link.username && !link.password) return link.href;
      } else if (row.type === "file" && typeof row.path === "string" && !row.path.startsWith("/")) {
        var file = new URL(row.path, base);
        var prefix = new URL("./" + section + "/", base);
        if (file.origin === base.origin && file.pathname.startsWith(prefix.pathname) && !file.search && !file.hash) return file.href;
      }
    } catch (_e) {}
    return null;
  }
  function render(def, data, base) {
    var list = document.getElementById(def.list);
    var count = document.getElementById(def.count);
    list.replaceChildren();
    var shown = 0;
    (Array.isArray(data) ? data : []).forEach(function (row) {
      var href = safeUrl(row, def.name, base);
      if (!href) return;
      var li = document.createElement("li");
      var a = document.createElement("a");
      var icon = document.createElement("span");
      var name = document.createElement("span");
      a.href = href;
      a.rel = "noopener noreferrer";
      a.target = "_blank";
      icon.className = "material-icon";
      icon.setAttribute("aria-hidden", "true");
      icon.textContent = row.type === "link" ? "🔗" : "📄";
      name.textContent = row.name;
      a.append(icon, name);
      li.appendChild(a);
      list.appendChild(li);
      shown++;
    });
    count.textContent = shown + "개";
    if (!shown) empty(list, "등록된 자료가 없습니다.");
  }
  async function loadStudentView() {
    var base = new URL("./", document.baseURI);
    var status = document.getElementById("status");
    try {
      var response = await fetch(new URL("./data/catalog.json", base), { cache: "no-store", credentials: "omit" });
      if (!response.ok) throw new Error("HTTP_ERROR");
      var catalog = await response.json();
      if (!catalog || catalog.schemaVersion !== 1) throw new Error("INVALID_CATALOG");
      categories.forEach(function (def) { render(def, catalog[def.name], base); });
      status.textContent = "자료 목록을 불러왔습니다. 자료는 새 탭에서 열립니다.";
      status.classList.remove("error");
    } catch (_e) {
      categories.forEach(function (def) {
        empty(document.getElementById(def.list), "자료 목록 조회에 실패했습니다. 새로고침해 주세요.");
        document.getElementById(def.count).textContent = "확인 불가";
      });
      status.textContent = "자료 목록을 불러올 수 없습니다. 잠시 후 다시 시도해 주세요.";
      status.classList.add("error");
    }
  }
  window.addEventListener("DOMContentLoaded", loadStudentView);
})();
