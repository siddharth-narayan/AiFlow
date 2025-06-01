import { schemaFetch } from "../fetcher";

class TritonApiInstance {
    url: string;

    constructor(url: string, options: any) {
        this.url = url
    }

    async getModels() {
        schemaFetch(`${url}/v2/repository/index`, { method: "POST"})
    }
}