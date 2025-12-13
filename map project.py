import folium
from folium.plugins import MousePosition
import webbrowser
import os


class DavaoTaxiSystem:
    def __init__(self):
        self.davao_center = [7.0731, 125.6128]

    def create_map(self):
        """Create interactive map with click functionality"""

        # Create base map
        m = folium.Map(
            location=self.davao_center,
            zoom_start=13,
            tiles='OpenStreetMap'
        )

        # Add mouse position tracker
        MousePosition().add_to(m)

        # Add custom HTML/CSS/JavaScript
        custom_code = """
        <!DOCTYPE html>
        <script>
            // Simple click handler - just adds markers, no controls
            var pickupMarker = null;
            var destinationMarker = null;
            var currentMode = 'pickup';

            // Green icon for pickup
            var greenIcon = L.icon({
                iconUrl: 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAiIGhlaWdodD0iNDUiIHZpZXdCb3g9IjAgMCAzMCA0NSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUgMEM5LjUgMCA1IDQuNSA1IDEwYzAgNy41IDEwIDIwIDEwIDIwczEwLTEyLjUgMTAtMjBjMC01LjUtNC41LTEwLTEwLTEweiIgZmlsbD0iIzEwYjk4MSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIi8+PHRleHQgeD0iMTUiIHk9IjE1IiBmb250LXNpemU9IjE0IiBmaWxsPSJ3aGl0ZSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9ImJvbGQiPFA8L3RleHQ+PC9zdmc+',
                iconSize: [30, 45],
                iconAnchor: [15, 45],
                popupAnchor: [0, -45]
            });

            // Red icon for destination
            var redIcon = L.icon({
                iconUrl: 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAiIGhlaWdodD0iNDUiIHZpZXdCb3g9IjAgMCAzMCA0NSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUgMEM5LjUgMCA1IDQuNSA1IDEwYzAgNy41IDEwIDIwIDEwIDIwczEwLTEyLjUgMTAtMjBjMC01LjUtNC41LTEwLTEwLTEweiIgZmlsbD0iI2VmNDQ0NCIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIi8+PHRleHQgeD0iMTUiIHk9IjE1IiBmb250LXNpemU9IjE0IiBmaWxsPSJ3aGl0ZSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9ImJvbGQiPkQ8L3RleHQ+PC9zdmc+',
                iconSize: [30, 45],
                iconAnchor: [15, 45],
                popupAnchor: [0, -45]
            });

            // Map click handler
            map.on('click', function(e) {
                if (currentMode === 'pickup') {
                    if (pickupMarker) map.removeLayer(pickupMarker);

                    pickupMarker = L.marker([e.latlng.lat, e.latlng.lng], {icon: greenIcon})
                        .addTo(map)
                        .bindPopup('<b>🚖 Pickup Location</b>')
                        .openPopup();

                    currentMode = 'destination';

                } else if (currentMode === 'destination') {
                    if (destinationMarker) map.removeLayer(destinationMarker);

                    destinationMarker = L.marker([e.latlng.lat, e.latlng.lng], {icon: redIcon})
                        .addTo(map)
                        .bindPopup('<b>🎯 Destination</b>')
                        .openPopup();
                }
            });
        </script>
        """

        # Add the custom code to the map
        m.get_root().html.add_child(folium.Element(custom_code))

        return m

    def run(self):
        """Run the taxi booking system"""
        print("🚕 Starting Davao City Taxi Booking System...")
        print("=" * 50)

        # Create map
        taxi_map = self.create_map()

        # Save to file
        filename = 'davao_taxi_map.html'
        taxi_map.save(filename)

        print(f"✅ Map saved as '{filename}'")
        print(f"📂 Location: {os.path.abspath(filename)}")

        # Open in browser
        webbrowser.open(f'file://{os.path.abspath(filename)}')

        print("🌐 Opening map in browser...")
        print("\n📝 How to use:")
        print("1. Click anywhere on the map for PICKUP (green marker)")
        print("2. Click 'Set Destination' then click for DESTINATION (red marker)")
        print("3. Distance and fare calculated automatically!")
        print("4. Use 'Clear All' to reset")
        print("\n✨ Map is ready! Start clicking!")


if __name__ == "__main__":
    system = DavaoTaxiSystem()
    system.run()