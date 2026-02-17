"use client";

import { useState } from "react";
import { getProducts } from "../services";
import { Product } from "../types";

export function useProducts() {

  const [products, setProducts] =
    useState<Product[]>([]);

  const [cursor, setCursor] =
    useState<string>();

  const [hasMore, setHasMore] =
    useState(false);

  async function loadProducts(
    params?: any
  ) {

    const data =
      await getProducts(params);

    setProducts(data.data);

    setCursor(data.next_cursor);

    setHasMore(data.has_more);

  }

  return {

    products,

    cursor,

    hasMore,

    loadProducts

  };

}
