import { z } from "zod"

export let index = z.array(
    z.object({
        name: z.string(),
        version: z.string().optional(),
        state: z.string(),
        reason: z.string()
    })
)