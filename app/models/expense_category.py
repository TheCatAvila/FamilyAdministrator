from app.database.db_connection import Database

class ExpenseCategory:
    def __init__(self, id: int = None, name: str = None):
        self.id = id
        self.name = name
    
    def get_all(self):
        """Obtiene todas las categorías de egresos."""
        try:
            query = """SELECT 
                            ec.id, 
                            ec.name, 
                            SUM(es.budget) AS total_budget
                        FROM 
                            expense_category ec
                        JOIN 
                            expense_subcategory es ON ec.id = es.category_id
                        GROUP BY 
                            ec.id, ec.name;
                    """
            with Database() as db:
                db.execute(query)
                categories = db.fetchall()
            
            return {"success": True, "categories": categories}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}
    
    def get_select_data(self):
        """Obtiene los nombres de todas las categorías de egresos."""
        try:
            query = "SELECT id, name FROM expense_category"
            with Database() as db:
                db.execute(query)
                categories = db.fetchall()
            
            return {"success": True, "categories": categories}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}
    
    def get_id_by_name(self):
        """Obtiene el ID de una categoría de egresos por su nombre."""
        try:
            query = "SELECT id FROM expense_category WHERE name = %s"
            values = (self.name,)
            with Database() as db:
                db.execute(query, values)
                category_id = db.fetchone()
            
            if category_id:
                return {"success": True, "id": category_id['id']}
            else:
                return {"success": False, "error": "Categoría no encontrada."}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}

    def create(self):
        """Crea una nueva categoría de egresos."""
        try:
            query = "INSERT INTO expense_category (name) VALUES (%s)"
            values = (self.name,)

            with Database() as db:
                db.execute(query, values)
                db.commit()

            return {"success": True, "message": "Categoría creada exitosamente."}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}