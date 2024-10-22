在 Linux 中，你可以通过以下几种方法来计算特定 Docker 容器（如包含 K18016 关键字的容器）占用的资源（CPU、内存等）。这些方法依赖于 Docker 命令和一些常见的 Linux 工具。

1. 使用 docker stats
docker stats 命令可以实时显示所有容器的资源使用情况，类似 top 命令的功能。你可以过滤出包含 K18016 的容器：

bash
複製程式碼
docker stats $(docker ps --filter "name=K18016" --format "{{.ID}}")
这会显示与 K18016 相关的容器的 CPU、内存、网络、磁盘使用等信息。

如果你只想看单个容器的资源使用情况，可以使用：

bash
複製程式碼
docker stats <container_id_or_name>
2. 使用 docker inspect 获取资源限制
如果你想查看 Docker 容器的资源限制（如 CPU 限制、内存限制等），可以使用 docker inspect 命令：

bash
複製程式碼
docker inspect <container_id_or_name> --format='{{.HostConfig.Memory}} {{.HostConfig.CpuQuota}} {{.HostConfig.CpuPeriod}}'
这会返回容器的内存限制（以字节为单位）、CPU 配额和 CPU 时间周期。

3. 使用 ps 和 grep 结合 docker top
你可以通过 docker top 命令获取容器内部进程的 PID，然后使用 ps 命令获取这些进程的资源占用情况：

bash
複製程式碼
docker top <container_id_or_name>
这会列出容器内部运行的进程及其 PID。然后，你可以使用 ps 查看特定进程的资源使用情况：

bash
複製程式碼
ps -p <pid> -o %cpu,%mem
4. 使用 cgroups 统计资源使用情况
Docker 容器使用 cgroups 来管理资源。你可以通过查看 cgroups 文件系统中的数据来了解容器的资源使用情况。

首先找到与容器 K18016 相关的 cgroup 路径：

bash
複製程式碼
docker inspect --format '{{.Id}}' <container_id_or_name>
然后你可以通过以下命令查看 CPU 使用情况（以秒为单位）：

bash
複製程式碼
cat /sys/fs/cgroup/cpu/docker/<container_id>/cpuacct.usage
查看内存使用情况：

bash
複製程式碼
cat /sys/fs/cgroup/memory/docker/<container_id>/memory.usage_in_bytes
5. 结合 pidstat 监控容器内部进程
你可以使用 pidstat 命令监控特定容器内部进程的资源使用情况，前提是你知道容器内部某个进程的 PID。

bash
複製程式碼
pidstat -p <pid> 1
这个命令会每秒刷新一次指定进程的资源占用情况。

6. 使用 docker system df 查看磁盘使用情况
如果你想查看 Docker 容器使用的磁盘空间，可以使用：

bash
複製程式碼
docker system df
这样你可以估算与容器相关的镜像、容器、卷等占用的磁盘资源。
