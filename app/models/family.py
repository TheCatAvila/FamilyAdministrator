from app.database.db_connection import Database

class Family:
    def __init__(self, id: int = None, name: str = None):
        self.id = id
        self.name = name
    
    def get(self):
        """Obtiene todas las familias asociadas al usuario logeado."""
        try:
            query = "SELECT id, name FROM family WHERE id = %s"
            values = (self.id,)
            with Database() as db:
                db.execute(query, values)
                families = db.fetchall()
            
            return {"success": True, "families": families}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}

    def create(self):
        """Crea una nueva familia al usuario logeado."""
        try:
            query = "INSERT INTO family (name) VALUES (%s)"
            values = (self.name,)

            with Database() as db:
                db.execute(query, values)
                family_id = db.last_insert_id()
                db.commit()

            return {"success": True, "message": "Familia creada exitosamente.", "family_id": family_id}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}
    
    def associate_with_user(self, user_id: int):
        """Asocia una familia a un usuario."""
        try:
            query = "INSERT INTO user_family (user_id, family_id, role_id) VALUES (%s, %s, %s)"
            values = (user_id, self.id, 2)

            with Database() as db:
                db.execute(query, values)
                db.commit()

            return {"success": True, "message": "Familia asociada al usuario exitosamente."}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}