# Agricultural Drone Simulation with AirSim

A comprehensive simulation project demonstrating the use of drones in precision agriculture, built using Microsoft AirSim and Unreal Engine.

## 🚁 Project Overview

This project focuses on developing and simulating an agricultural drone for precision farming applications. The drone performs automated field coverage using a lawnmower flight pattern, enabling tasks such as:

- Crop monitoring and health assessment
- Field mapping and surveying  
- Precision spraying applications
- Agricultural data collection

## 🛠️ Technologies Used

- **[Microsoft AirSim](https://github.com/microsoft/AirSim)** - Drone physics simulation and control
- **Unreal Engine** - Realistic 3D agricultural environment
- **Python** - Flight control scripting and automation
- **NumPy** - Mathematical computations for flight path planning

## 📁 Project Structure

```
agricultural-drone-airsim/

├── Drone_Airsim.py           # Main drone control script
├── Drone_in_Agriculture_Report_Final.pdf  # Research report
└── simulation/                    # Simulation video
└── airsim_settings.json       # AirSim configuration
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🚀 Quick Start

### Prerequisites

- **Unreal Engine 4.27 or later** - [Download here](https://www.unrealengine.com/)
- **Microsoft AirSim** - Follow setup instructions below
- **Python 3.7+** with pip
- **Git** for version control

### Step 1: AirSim Setup

**Important**: You must set up AirSim with Unreal Engine before running this project.

1. **Follow the official AirSim setup guide**: 
   - 📖 **[AirSim Setup Instructions](https://github.com/microsoft/AirSim)**
   - Choose your platform (Windows/Linux/macOS)
   
2. **For Windows users**:
   ```bash
   # Clone AirSim repository
   git clone https://github.com/Microsoft/AirSim.git
   cd AirSim
   
   # Build AirSim
   build.cmd
   ```

3. **For Linux users**:
   ```bash
   # Clone AirSim repository  
   git clone https://github.com/Microsoft/AirSim.git
   cd AirSim
   
   # Build AirSim
   ./setup.sh
   ./build.sh
   ```

4. **Create Unreal Engine Project**:
   - Follow AirSim's guide to create a new UE project or use existing environments
   - Popular options: AirSimNH (Neighborhood), Blocks Environment, or create custom agricultural environment

### Step 2: Project Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/agricultural-drone-airsim.git
   cd agricultural-drone-airsim
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AirSim settings**:
   ```bash
   # Copy the configuration file to your AirSim settings directory
   # Windows: Copy config/airsim_settings.json to ~/Documents/AirSim/settings.json
   # Linux: Copy config/airsim_settings.json to ~/Documents/AirSim/settings.json
   ```

### Step 3: Run the Simulation

1. **Launch Unreal Engine** with your agricultural environment
2. **Press Play** in the UE editor
3. **Run the drone script**:
   ```bash
   python src/Drone_Airsim.py
   ```

### Troubleshooting

- **Connection Issues**: Ensure AirSim is running in Unreal Engine before executing the Python script
- **Import Errors**: Verify all dependencies are installed with `pip list`
- **Performance Issues**: Lower graphics settings in Unreal Engine for better simulation performance
- **Path Issues**: Make sure field corner coordinates match your Unreal Engine environment scale

For detailed AirSim setup help, visit the [official documentation](https://microsoft.github.io/AirSim/).

## 🎯 Flight Pattern Algorithm

The drone uses an intelligent lawnmower pattern algorithm that:

1. **Analyzes field boundaries** from 4 corner coordinates
2. **Calculates optimal flight strips** based on configurable spacing
3. **Alternates direction** for each strip to minimize flight time
4. **Maintains consistent altitude** throughout the mission
5. **Handles irregular field shapes** automatically

### Key Parameters

- `STRIP_SPACING`: Distance between parallel flight strips (default: 50m)
- `FLIGHT_SPEED`: Drone velocity during mission (default: 10 m/s)
- Field corners defined in UE world coordinates

## 📊 Performance Results

From our simulation testing:

- **Coverage Efficiency**: 100% field coverage with minimal overlap
- **Flight Time**: ~5 minutes for standard field at 3 m/s
- **Altitude Stability**: Consistent 10m altitude maintained
- **Environmental Adaptation**: Successful operation under various wind conditions

## 🔬 Research Highlights

This project demonstrates:

- Cost-effective drone development through simulation
- Precision agriculture applications and benefits
- Integration of modern simulation tools for agricultural research
- Practical flight algorithms for real-world deployment

For detailed technical analysis, see our [research report](docs/Drone_in_Agriculture_Report_Final.pdf).

## 🌱 Agricultural Applications

The simulated drone can support various farming operations:

- **Crop Health Monitoring**: Early detection of plant stress and disease
- **Precision Spraying**: Targeted application of fertilizers and pesticides  
- **Field Mapping**: Generation of detailed agricultural maps
- **Irrigation Management**: Monitoring of water distribution and soil moisture

## 🔧 Configuration

The drone's behavior can be customized by modifying parameters in `Drone_Airsim.py`:

```python
# Flight parameters
STRIP_SPACING = 50.0   # meters between each pass
FLIGHT_SPEED  = 10.0   # m/s

# Field boundaries (X, Y, Z coordinates)
raw_corners = np.array([
    [ 76.9297, -77.8449, 8.790],
    [ 77.9950,  76.6607, 8.790],
    [-76.9277,  76.4324, 8.790],
    [-74.0643, -77.4082, 8.790]
])
```

## 🎥 Demo

![Drone Flight Demo](docs/images/drone_flight_demo.gif)

*Drone executing lawnmower pattern over simulated agricultural field*

## 🚀 Future Enhancements

- **Advanced Sensors**: Integration of multispectral and thermal cameras
- **AI-Powered Analytics**: Real-time crop health analysis
- **Multi-Drone Coordination**: Swarm intelligence for large-scale operations
- **Dynamic Path Planning**: Adaptive flight patterns based on field conditions
- **Weather Integration**: Enhanced environmental simulation

## 👥 Contributors

- **Ashutosh Kumar** - B.Tech ECE, IIIT Naya Raipur
- **Prateek Rathi** - B.Tech ECE, IIIT Naya Raipur  
- **Sanskar Sharma** - B.Tech ECE, IIIT Naya Raipur

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Microsoft AirSim Team](https://github.com/microsoft/AirSim)** - For providing the excellent simulation platform
- **Unreal Engine Community** - For the powerful 3D development environment
- **Agricultural Technology Researchers** - For pioneering drone applications in farming
- **International Institute of Information Technology, Naya Raipur** - For academic support and guidance

## 🔗 Useful Links

- **[Microsoft AirSim Repository](https://github.com/microsoft/AirSim)** - Main AirSim project and documentation
- **[AirSim Documentation](https://microsoft.github.io/AirSim/)** - Comprehensive setup and API guides
- **[Unreal Engine](https://www.unrealengine.com/)** - Download and documentation
- **[AirSim Python API](https://microsoft.github.io/AirSim/api_docs/html/index.html)** - Python API reference
- **[Agricultural Drone Applications](https://www.fao.org/3/ca5530en/ca5530en.pdf)** - FAO report on drone use in agriculture

## 📞 Contact

For questions or collaboration opportunities:
- Email: ashutosh23101@iiitnr.edu.in
- Project Link: https://github.com/yourusername/agricultural-drone-airsim

---

⭐ **Star this repository if you found it helpful!**
