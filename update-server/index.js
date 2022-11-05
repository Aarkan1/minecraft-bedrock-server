const { writeFileSync } = require("fs");
const { execSync } = require("child_process");
const { join } = require("path");

module.exports = (config) => {
    let version = execSync(`${__dirname}/scrape.py`)
        .toString()
        .replace("\n", "");

    const currentVersion = config["minecraft-server-version"];

    if (!version || version == currentVersion) return;

    console.warn("New bedrock server version available");
    config["minecraft-server-version"] = version;

    writeFileSync(
        join(__dirname, "..", "config.json"),
        JSON.stringify(config, null, 2)
    );
    execSync("pm2 restart mc-server");
};
