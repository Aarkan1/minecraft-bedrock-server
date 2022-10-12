import { $ } from "zx";
$.verbose = false;
import * as url from "url";
const __dirname = url.fileURLToPath(new URL(".", import.meta.url));
import { writeFileSync } from "fs";
import { execSync } from "child_process";
import { join } from "path";

export const version = async (config) => {
    let version = (await $`${__dirname}/scrape.py`).stdout.replace("\n", "");

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
