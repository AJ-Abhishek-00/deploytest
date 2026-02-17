"use client";

import { useEffect, useState } from "react";
import { fetchProducts } from "@/services/productService";

export default function ProductTable() {

  const [products, setProducts] = useState<any[]>([]);

  const [cursor, setCursor] = useState<string | undefined>(undefined);

  // FIX: initialize with undefined to represent first page
  const [cursorHistory, setCursorHistory] =
    useState<(string | undefined)[]>([undefined]);

  const [hasMore, setHasMore] = useState(false);

  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("");
  const [sortBy, setSortBy] = useState("created_at");
  const [sortOrder, setSortOrder] = useState("desc");


  // Load Products
  const loadProducts = async (
    cursorValue?: string,
    isNext: boolean = false,
    isPrevious: boolean = false
  ) => {

    try {

      const data = await fetchProducts(
        cursorValue,
        10,
        search,
        sortBy,
        sortOrder,
        category
      );

      setProducts(data.data);

      setCursor(data.next_cursor);

      setHasMore(data.has_more);

      // FIX: when moving next, push next cursor into history
      if (isNext && data.next_cursor) {

        setCursorHistory(prev => [
          ...prev,
          data.next_cursor
        ]);

      }

      // FIX: when moving previous, remove last history entry
      if (isPrevious) {

        setCursorHistory(prev =>
          prev.slice(0, prev.length - 1)
        );

      }

    } catch (error) {

      console.error(error);

    }

  };


  // Initial load
  useEffect(() => {

    loadProducts(undefined);

  }, []);



  // PREVIOUS PAGE HANDLER
  const handlePrevious = () => {

    if (cursorHistory.length <= 1) return;

    const previousCursor =
      cursorHistory[cursorHistory.length - 2];

    loadProducts(previousCursor, false, true);

  };



  return (

    <div className="bg-white dark:bg-gray-900 text-black dark:text-white">

      <h2 className="text-2xl font-semibold mb-4">
        Products
      </h2>

      {/* Filters */}
      <div className="flex flex-wrap gap-3 mb-4">

        <input
          placeholder="Search by name"
          value={search}
          onChange={(e)=>setSearch(e.target.value)}
          className="bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 text-black dark:text-white p-2 rounded w-48"
        />

        <input
          placeholder="Filter by category"
          value={category}
          onChange={(e)=>setCategory(e.target.value)}
          className="bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 text-black dark:text-white p-2 rounded w-48"
        />

        <select
          value={sortBy}
          onChange={(e)=>setSortBy(e.target.value)}
          className="bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 text-black dark:text-white p-2 rounded"
        >
          <option value="created_at">Created</option>
          <option value="price">Price</option>
          <option value="rating">Rating</option>
        </select>

        <select
          value={sortOrder}
          onChange={(e)=>setSortOrder(e.target.value)}
          className="bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 text-black dark:text-white p-2 rounded"
        >
          <option value="desc">Desc</option>
          <option value="asc">Asc</option>
        </select>

        <button
          onClick={()=>loadProducts(undefined)}
          className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
        >
          Apply
        </button>

      </div>


      {/* Table */}
      <div className="overflow-x-auto">

        <table className="w-full border border-gray-300 dark:border-gray-700">

          <thead className="bg-gray-200 dark:bg-gray-800">

            <tr>
              <th className="p-3 border border-gray-300 dark:border-gray-700 text-left">ID</th>
              <th className="p-3 border border-gray-300 dark:border-gray-700 text-left">Name</th>
              <th className="p-3 border border-gray-300 dark:border-gray-700 text-left">Category</th>
              <th className="p-3 border border-gray-300 dark:border-gray-700 text-left">Price</th>
              <th className="p-3 border border-gray-300 dark:border-gray-700 text-left">Rating</th>
            </tr>

          </thead>

          <tbody>

            {products.map((product) => (

              <tr key={product.id}
                  className="hover:bg-gray-100 dark:hover:bg-gray-800">

                <td className="p-3 border border-gray-300 dark:border-gray-700">
                  {product.id}
                </td>

                <td className="p-3 border border-gray-300 dark:border-gray-700">
                  {product.name}
                </td>

                <td className="p-3 border border-gray-300 dark:border-gray-700">
                  {product.category}
                </td>

                <td className="p-3 border border-gray-300 dark:border-gray-700">
                  ₹{product.price}
                </td>

                <td className="p-3 border border-gray-300 dark:border-gray-700">
                  {product.rating}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>


      {/* Pagination */}
      <div className="mt-4 flex gap-3">

        {/* Previous Button */}
        <button
          disabled={cursorHistory.length <= 1}
          onClick={handlePrevious}
          className="px-4 py-2 rounded bg-gray-600 text-white disabled:opacity-50"
        >
          Previous Page
        </button>


        {/* Next Button */}
        <button
          disabled={!hasMore || !cursor}
          onClick={() => loadProducts(cursor, true)}
          className={`px-4 py-2 rounded text-white ${
            hasMore
              ? "bg-green-600 hover:bg-green-700"
              : "bg-gray-400 cursor-not-allowed"
          }`}
        >
          Next Page
        </button>

      </div>

    </div>

  );

}
