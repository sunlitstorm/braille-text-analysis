const brailleMap = {
    // Letters
    a: "⠁", b: "⠃", c: "⠉", d: "⠙", e: "⠑",
    f: "⠋", g: "⠛", h: "⠓", i: "⠊", j: "⠚",
    k: "⠅", l: "⠇", m: "⠍", n: "⠝", o: "⠕",
    p: "⠏", q: "⠟", r: "⠗", s: "⠎", t: "⠞",
    u: "⠥", v: "⠧", w: "⠺", x: "⠭", y: "⠽",
    z: "⠵",

    // Numbers
    "1": "⠼⠁",
    "2": "⠼⠃",
    "3": "⠼⠉",
    "4": "⠼⠙",
    "5": "⠼⠑",
    "6": "⠼⠋",
    "7": "⠼⠛",
    "8": "⠼⠓",
    "9": "⠼⠊",
    "0": "⠼⠚",

    // Punctuation
    ".": "⠲",
    ",": "⠂",
    "!": "⠖",
    "?": "⠦",
    ";": "⠆",
    ":": "⠒",
    "-": "⠤",
    "'": "⠄",
    "\"": "⠶",
    "(": "⠐⠣",
    ")": "⠐⠜",
    "/": "⠌",
    "&": "⠯",
    "@": "⠈⠁",
    "#": "⠼",
    "%": "⠨⠴",
    "*": "⠔",

    // Space
    " ": " "
};

function translateText() {
    const text = document
        .getElementById("inputText")
        .value
        .toLowerCase();

    const result = text
        .split("")
        .map(char => brailleMap[char] || char)
        .join("");

    document.getElementById("output").textContent = result;
}