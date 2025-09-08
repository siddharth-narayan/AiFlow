import { z } from "zod";

export let tritonDataTypes = z.enum(["TYPE_BYTES", "TYPE_STRING"]);

export let modelInput = z.object({
    name: z.string(),
    data_type: z.string(),
    dims: z.array(z.number()),
    optional: z.boolean(),
});

export let modelOutput = z.object({
    name: z.string(),
    data_type: tritonDataTypes,
    dims: z.array(z.number()),
});

export let modelIndexResponse = z.array(
    z.object({
        name: z.string(),
        version: z.string().optional(),
        state: z.enum(["READY", "UNREADY"]),
    }),
);

export let modelInfoResponse = z.object({
    name: z.string(),
    input: z.array(modelInput),
    output: z.array(modelOutput),
});
