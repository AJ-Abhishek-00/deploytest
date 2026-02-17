import { api } from "./api";

export const fetchProducts = async (
  cursor?: string,
  limit = 10,
  search?: string,
  sortBy?: string,
  sortOrder?: string,
  category?: string
) => {

  const params: any = {
    limit,
    sort_by: sortBy,
    sort_order: sortOrder,
  };

  if (cursor)
    params.cursor = cursor;

  if (search)
    params.search = search;

  if (category)
    params.category = category;

  const response =
    await api.get("/products", { params });

  return response.data;

};
