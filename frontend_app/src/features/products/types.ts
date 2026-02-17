export interface Product {

  id: number;

  name: string;

  category: string;

  price: number;

  rating: number;

  createdAt: string;

}

export interface ProductResponse {

  data: Product[];

  next_cursor?: string;

  has_more: boolean;

}
