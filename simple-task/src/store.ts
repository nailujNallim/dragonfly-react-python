import { create } from "zustand";

type Todo = {
  id: number;
  title: string;
  completed: boolean;
};

type CreateTodo = {
  title: string;
};

type TodoStore = {
  todos: Todo[];
  fetchTodos: () => void;
  addTodo: (todo: CreateTodo) => void;
};

const URL = "http://localhost:8000/api";

export const useStore = create<TodoStore>((set) => ({
  todos: [],
  fetchTodos: async () => {
    try {
      const response = await fetch(`${URL}/todos`);
      const todos = await response.json();
      set({ todos });
    } catch (error) {
      console.error("Error fetching todos:", error);
    }
  },
  addTodo: async (todo) => {
    try {
      const response = await fetch(`${URL}/todos`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(todo),
      });
      const createdTodo = await response.json();
      set((state) => ({ todos: [...state.todos, createdTodo] }));
    } catch (error) {
      console.error("Error creating todo:", error);
    }
  }
}));
