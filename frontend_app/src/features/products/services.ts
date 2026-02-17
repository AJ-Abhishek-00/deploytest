import { api } from "@/services/api";
import { ProductResponse } from "./types";

export async function getProducts(
  params: any
): Promise<ProductResponse> {

  const res =
    await api.get("/products", {
      params
    });

  return res.data;

}
