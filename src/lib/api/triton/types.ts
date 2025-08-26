import { z } from "zod"
import type { modelInfoResponse } from "./api-schema"

export type ModelType = z.infer<typeof modelInfoResponse>