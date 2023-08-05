#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <libudev.h>           // for udev functions and structures
#include <fcntl.h>             // for open function
#include <sys/ioctl.h>         // for ioctl function
#include <linux/videodev2.h>   // for v4l2_capability structure and VIDIOC_QUERYCAP constant
#include <string>  // include the header for std::string
#include <cwchar>  // include the header for wcscmp
#include <locale>


namespace py = pybind11;
int32_t indexList = -1;


#define TOF_VID "2560"
#define TOF_PID "C0D6"


typedef struct
{
    char deviceName[50];
    char vid[5];
    char pid[5];
    char devicePath[500];
    char serialNo[50];
}DeviceInfo;

bool isValidNode(std::string deviceNodeName);
bool getDeviceInfo(uint32_t deviceIndex, DeviceInfo* gDevice);

bool initialize()
    {
        // Device Enumeration
        struct udev *udev;
        struct udev_enumerate *enumerate;
        struct udev_list_entry *device, *dev_list_entry;
        struct udev_device *dev,*pdev;
        std::string vid, pid, path,device_node;
        uint32_t device_node_count=0;


        udev = udev_new();

        if(!udev)
        	return false;
            //return DEPTHVISTAError::setErrno(Result::NotInitialized);

        enumerate = udev_enumerate_new(udev);
        udev_enumerate_add_match_subsystem(enumerate, "video4linux");
        udev_enumerate_scan_devices(enumerate);
        device = udev_enumerate_get_list_entry(enumerate);

        indexList = 0;
        udev_list_entry_foreach(dev_list_entry, device)
        {
            path = udev_list_entry_get_name(dev_list_entry);
            dev = udev_device_new_from_syspath(udev, path.c_str());
            device_node = udev_device_get_devnode(dev);
            if(isValidNode(device_node))
            {
				pdev = udev_device_get_parent_with_subsystem_devtype(dev, "usb", "usb_device");
				if (!pdev){
                    indexList=-1;
                    //return DEPTHVISTAError::setErrno(Result::NotInitialized);
                    return false;
				}
				vid = udev_device_get_sysattr_value(pdev, "idVendor");
				pid = udev_device_get_sysattr_value(pdev, "idProduct");
                if(!strcmp(vid.c_str(),TOF_VID) && !strcmp(pid.c_str(),TOF_PID))
                {
					sscanf(&device_node[10], "%d", &device_node_count);
					indexList|=(1<<device_node_count);
				}
            }
			udev_device_unref(dev);
        }
        udev_enumerate_unref(enumerate);
        udev_unref(udev);
		// end of Device Enumeration
        //return DEPTHVISTAError::setErrno(Result::Ok);
        return true;
  }

    bool isInitialized()
	{
		if(indexList<0)
            //return DEPTHVISTAError::setErrno(Result::NotInitialized);
            return false;
        //return DEPTHVISTAError::setErrno(Result::NotDeInitialized);
        return false;
	}

    bool deInitialize()
    {
        indexList = -1;
        //return DEPTHVISTAError::setErrno(Result::Ok);
        return true;
    }

    bool isValidNode(std::string deviceNodeName)
	{
		int device_handle;
        struct v4l2_capability cam_cap;
        if ((device_handle= open(deviceNodeName.c_str(), O_RDWR|O_NONBLOCK, 0)) < 0) 
        {
            //return DEPTHVISTAError::setErrno(Result::CameraNotOpened);
            return false;
        }
        /* Check if the device is capable of streaming */
        if(ioctl(device_handle, VIDIOC_QUERYCAP, &cam_cap) < 0) 
        {
            close(device_handle);
            //return DEPTHVISTAError::setErrno(Result::SysCallFail);
            return false;
        }
        close(device_handle);

        if (cam_cap.device_caps & V4L2_CAP_META_CAPTURE)
        	return false;
            //return DEPTHVISTAError::setErrno(Result::InvalidNode);
        else
        	return true;
            //return DEPTHVISTAError::setErrno(Result::Ok);
    }


    bool getDeviceCount(uint32_t *gDeviceCount)
    {
		initialize();
		int list=indexList;
		*gDeviceCount = 0;
        if(!indexList){
            //return DEPTHVISTAError::setErrno(Result::NoDeviceConnected);
            return false;
        }
        while (list)
        {
            list &= (list-1);
            *gDeviceCount+=1;
        }
        //return DEPTHVISTAError::setErrno(Result::Ok);
        return true;
	}


    bool isValidIndex(uint32_t deviceIndex)
	{
		uint32_t device_count;
		if(getDeviceCount(&device_count))
		{
			return false;
            //return DEPTHVISTAError::setErrno(Result::NoDeviceConnected);
		}
		if(deviceIndex > device_count || deviceIndex < 0)
			return false;
            //return DEPTHVISTAError::setErrno(Result::InvalidDeviceIndex);
        //return DEPTHVISTAError::setErrno(Result::Ok);
        return true;
	}


    bool getDeviceListInfo(uint32_t deviceCount,DeviceInfo* gDevicesList)
    {

        for (uint32_t index = 0; index < deviceCount; index++) {
            if(!getDeviceInfo(index,(gDevicesList+index))){
               // return Result::Others;
            	return false;
			}
		}
        //return DEPTHVISTAError::setErrno(Result::Ok);
        return true;
    }


    void getDevNodeNumber(uint32_t *nodeNo)
	{
		uint32_t auto_index = 0, count = 0;
		while(auto_index < 16){
        if((1<<auto_index) & indexList){
            if(count == *nodeNo){
                *nodeNo = auto_index;
                break;
	        }
	        count++;
	     }
	     auto_index++;
	   }
	}


    bool getDeviceInfo(uint32_t deviceIndex, DeviceInfo* gDevice)
    {
		uint32_t device_count;
		std::stringstream device_name;
		if (isValidIndex(deviceIndex) < 0) {
           // return DEPTHVISTAError::setErrno(Result::InvalidDeviceIndex);
			return false;
		}
		getDevNodeNumber(&deviceIndex);
		device_name <<"video"<<deviceIndex;
		struct udev *udev;
		struct udev_device *dev,*pdev;
		std::string vid, pid, path;

		udev = udev_new();

		if(!udev)
			return false;
            //return DEPTHVISTAError::setErrno(Result::Others);
		dev = udev_device_new_from_subsystem_sysname(udev,"video4linux",device_name.str().c_str());

		pdev = udev_device_get_parent_with_subsystem_devtype(dev, "usb", "usb_device");
		if (!pdev){
            //return DEPTHVISTAError::setErrno(Result::Others);
            return false;
		}
        /*
            *Inorder to assign const char* to char array...declare as
          const char* type and assign that particular value.
            *Then using strcpy, copy that to structure variables
        */

        const char* Device_Name = udev_device_get_sysattr_value(pdev, "product");
        const char* P_Id = udev_device_get_sysattr_value(pdev, "idProduct");
        const char* V_Id = udev_device_get_sysattr_value(pdev, "idVendor");
        const char* Serial_No = udev_device_get_sysattr_value(pdev, "serial");
        const char* Device_Path = udev_device_get_devnode(dev);

        strcpy(gDevice->deviceName, Device_Name);
        strcpy(gDevice->vid, V_Id);
        strcpy(gDevice->pid, P_Id);
        strcpy(gDevice->serialNo, Serial_No);
        strcpy(gDevice->devicePath, Device_Path);
		udev_device_unref(dev);
		udev_unref(udev);
        //return DEPTHVISTAError::setErrno(Result::Ok);
        return true;
  }
  
PYBIND11_MODULE(Enumerator_linux, m)
{
    m.def("getDeviceInfo", &getDeviceInfo, "getDeviceInfo");
    m.def("getDeviceCount", &getDeviceCount, "getDeviceCount");
	m.def("getDeviceListInfo", &getDeviceListInfo, "getDeviceListInfo");

	py::class_<DeviceInfo>(m, "DeviceInfo")
        .def(py::init<>())
        .def_property("deviceName",
            [](const DeviceInfo& info) {
                return py::array(py::buffer_info(
                    const_cast<char*>(info.deviceName),
                    sizeof(char),
                    py::format_descriptor<char>::format(),
                    1,
                    {50},
                    {sizeof(char)}
                ));
            },
            [](DeviceInfo& info, const py::array_t<char>& arr) {
                auto buf = arr.request();
                if (buf.size != 50)
                    throw std::runtime_error("Invalid array size");
                std::memcpy(info.deviceName, buf.ptr, buf.size * sizeof(char));
            }
        )
        .def_property("vid",
            [](const DeviceInfo& info) {
                return py::array(py::buffer_info(
                    const_cast<char*>(info.vid),
                    sizeof(char),
                    py::format_descriptor<char>::format(),
                    1,
                    {5},
                    {sizeof(char)}
                ));
            },
            [](DeviceInfo& info, const py::array_t<char>& arr) {
                auto buf = arr.request();
                if (buf.size != 5)
                    throw std::runtime_error("Invalid array size");
                std::memcpy(info.vid, buf.ptr, buf.size * sizeof(char));
            }
        )
        .def_property("pid",
            [](const DeviceInfo& info) {
                return py::array(py::buffer_info(
                    const_cast<char*>(info.pid),
                    sizeof(char),
                    py::format_descriptor<char>::format(),
                    1,
                    {5},
                    {sizeof(char)}
                ));
            },
            [](DeviceInfo& info, const py::array_t<char>& arr) {
                auto buf = arr.request();
                if (buf.size != 5)
                    throw std::runtime_error("Invalid array size");
                std::memcpy(info.pid, buf.ptr, buf.size * sizeof(char));
            }
        )
        .def_property("devicePath",
            [](const DeviceInfo& info) {
                return py::array(py::buffer_info(
                    const_cast<char*>(info.devicePath),
                    sizeof(char),
                    py::format_descriptor<char>::format(),
                    1,
                    {500},
                    {sizeof(char)}
                ));
            },
            [](DeviceInfo& info, const py::array_t<char>& arr) {
                auto buf = arr.request();
                if (buf.size != 500)
                    throw std::runtime_error("Invalid array size");
                std::memcpy(info.devicePath, buf.ptr, buf.size * sizeof(char));
            }
        )
        .def_property("serialNo",
            [](const DeviceInfo& info) {
                return py::array(py::buffer_info(
                    const_cast<char*>(info.serialNo),
                    sizeof(char),
                    py::format_descriptor<char>::format(),
                    1,
                    {50},
                    {sizeof(char)}
                ));
            },
            [](DeviceInfo& info, const py::array_t<char>& arr) {
                auto buf = arr.request();
                if (buf.size != 50)
                    throw std::runtime_error("Invalid array size");
               std::memcpy(info.serialNo, buf.ptr, buf.size * sizeof(char));}
);

}