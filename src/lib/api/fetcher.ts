import { z } from "zod"
import { modelInfoResponse } from "./triton/triton-inference-schema"

export async function schemaFetch<T extends z.ZodTypeAny>(args: Parameters<typeof fetch>, schema: T): Promise<z.infer<T>> {
    let response = await fetch(args[0], args[1])
    let json = await response.json()

    return schema.parse(json)
}
