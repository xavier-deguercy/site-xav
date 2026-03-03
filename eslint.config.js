module.exports = [
  {
    files: ["js/**/*.js"],
    languageOptions: {
      ecmaVersion: 2023,
      sourceType: "module",
      globals: {
        document: "readonly",
        URL: "readonly",
        window: "readonly"
      }
    },
    rules: {
      "no-unused-vars": ["error", { "args": "none" }]
    }
  }
];
