import type { z } from "zod";
import { schemaFetch } from "../fetcher";
import { modelIndexResponse, modelInfoResponse } from "./api-schema";

export class TritonApiInstance {
    url: string;
    ready: Promise<void>

    models!: z.infer<typeof modelInfoResponse>[];

    constructor(url: string, options?: any) {
        this.url = url;

        this.ready = this.fetchModels().then(async (models) => {
            this.models = await Promise.all(models.map(async model => {
                return { ...model, ...(await this.modelInfo(model.name)) }
            }))
        });

    }

    async fetchModels() {
        return schemaFetch([`${this.url}/v2/repository/index`, { method: "POST" }], modelIndexResponse)
    }

    async filterModels(
        inputType: string,
        outputType: string
    ) {
        await this.ready
        let filtered = this.models.filter(async (model) => {
            let containsCorrectInput =
                model.input.filter((input) => {
                    input.data_type == inputType;
                }).length > 0;

            let containsCorrectOutput =
                model.output.filter((output) => {
                    output.data_type == outputType;
                }).length > 0;

            return (
                containsCorrectInput && containsCorrectOutput && model.state == "READY"
            );
        });

        return filtered
    }

    async modelInfo(model_name: string) {
        return schemaFetch([`${this.url}/v2/models/${model_name}/config`], modelInfoResponse)
    }

    async infer(model_name: string, inputs: any) {
        console.log(inputs)
        return fetch(`${this.url}/${model_name}/infer`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                inputs: inputs,
                outputs: [{ name: "encoder_hidden_states" }],
            }),
        });
    }
}

let tritonEndpoint = "https://test.novaphaze.com";
export let triton = new TritonApiInstance(tritonEndpoint);

// [
//                     {
//                         name: "input_ids",
//                         shape: [1, input_ids.length],
//                         datatype: "INT32",
//                         // data: input_ids,
//                     },
//                 ],