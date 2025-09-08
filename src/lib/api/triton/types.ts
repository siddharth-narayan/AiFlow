import { z } from "zod";
import type {
    modelIndexResponse,
    modelInfoResponse,
    modelInput,
    modelOutput,
    tritonDataTypes,
} from "./api-schema";

export type DataType = z.infer<typeof tritonDataTypes>;
export type ModelInputType = z.infer<typeof modelInput>;
export type ModelOutputType = z.infer<typeof modelOutput>;
export type ModelType = z.infer<typeof modelInfoResponse>;
export type ModelIndexType = z.infer<typeof modelIndexResponse>;
