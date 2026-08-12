from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timer_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.middleware("http")(timer_middleware)

app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(issues_router)



# items = [
#     {"id": 1, "name": "Item 1", "description": "This is item 1"},
#     {"id": 2, "name": "Item 2", "description": "This is item 2"},
#     {"id": 3, "name": "Item 3", "description": "This is item 3"}

# ]


# @app.get("/health")
# def health_check():
#     return {"status": "healthy"}

# @app.get("/items")
# def get_items():
#     return items        

# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     for item in items:
#         if item["id"] == item_id:
#             return item
#     return {"error": "Item not found"}  

# @app.post("/items")
# def create_item(item: dict):
#     item_id = len(items) + 1
#     new_item = {"id": item_id, **item}
#     items.append(new_item)
#     return new_item
