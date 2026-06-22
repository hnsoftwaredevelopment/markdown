Project View model

Project View model

```C#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using JiraLogWork.Views;
using JiraLogWork.Models;
using System.Windows.Threading;

namespace JiraLogWork.ViewModels
{
	public class ProjectViewModel : ViewModelBase, IPresentationViewModel
	{

		private IEnumerable<IPresentationViewModel> _presentationViewModels;
		private Jira.REST.Jira _jira;
		private IEnumerable<NameValueModel> _boards;
		private IEnumerable<NameValueModel> _sprints;
		private IEnumerable<NameValueModel> _issues;
		private string _selectedBoard;
		private string _selectedSprint;
		private string _selectedIssue;
		private DispatcherTimer _timer = new DispatcherTimer();
		private int secondsElapsed = 0;
		private string _timeElapsed = "00:00:00";
		private string _message;
		private DateTime _selectedDate = DateTime.Now;

		public ProjectViewModel(IProjectView view, IEnumerable<IPresentationViewModel> presentationViewModels, Jira.REST.Jira jira)
		{
			this.Name = "Project Screen";
			this.Page = Pages.Project;
			this.View = view;
			_presentationViewModels = presentationViewModels;
			_jira = jira;

			InitCommands();
		}

		public string Name { get; set; }
		public Pages Page { get; set; }
		public IView View { get; set; }

		private void InitCommands()
		{
			Boards_Changed = new DelegateCommand(async _ =>
			{
				var getSprints = await _jira.GetBoardSprints(SelectedBoard.ToString());

				Sprints = getSprints.Where(x => x.State == "active")
									.Select(x => new NameValueModel
									{
										Name = x.Name,
										Value = x.Id.ToString()
									});
			});

			Sprints_Changed = new DelegateCommand(async _ =>
			{
				var issues = await _jira.GetIssuesByBoardAndSprint(SelectedBoard.ToString(), SelectedSprint.ToString());

				Issues = issues.Select(x => new NameValueModel
				{
					Name = x.Key,
					Value = x.Key
				});
			});

			LogWork = new DelegateCommand(async _ =>
			{
				if(string.IsNullOrEmpty(SelectedIssue))
				{

				} else
				{
					var worklog = await _jira.AddWorkLog(SelectedIssue, SelectedDate, secondsElapsed, Message);
				}
			});

			_timer.Tick += _timer_Tick;
			_timer.Interval = new TimeSpan(0, 0, 1);

			Start_Timer = new DelegateCommand(_ =>
			{
				_timer.Start();
			});

			Stop_Timer = new DelegateCommand(_ =>
			{
				_timer.Stop();
			});

			Reset_Timer = new DelegateCommand(_ =>
			{
				secondsElapsed = 0;
				TimeElapsed = new TimeSpan(0, 0, 0, secondsElapsed).ToString();
			});
		}

		private void _timer_Tick(object sender, EventArgs e)
		{
			secondsElapsed++;
			TimeElapsed = new TimeSpan(0, 0, 0, secondsElapsed).ToString();
		}

		// Boards

		public string SelectedBoard
		{
			get { return _selectedBoard; }
			set { this.SetField(ref this._selectedBoard, value, () => this.SelectedBoard); }
		}

		public IEnumerable<NameValueModel> Boards
		{
			get { return _boards; }
			set { this.SetField(ref this._boards, value, () => this.Boards); }
		}

		public DelegateCommand Boards_Changed { get; set; }

		// Sprints

		public string SelectedSprint
		{
			get { return _selectedSprint; }
			set { this.SetField(ref this._selectedSprint, value, () => this.SelectedSprint); }
		}

		public IEnumerable<NameValueModel> Sprints
		{
			get { return _sprints; }
			set { this.SetField(ref this._sprints, value, () => this.Sprints); }
		}
		public DelegateCommand Sprints_Changed { get; set; }


		// Issues

		public string SelectedIssue
		{
			get { return _selectedIssue; }
			set { this.SetField(ref this._selectedIssue, value, () => this.SelectedIssue); }
		}

		public IEnumerable<NameValueModel> Issues
		{
			get { return _issues; }
			set { this.SetField(ref this._issues, value, () => this.Issues); }
		}
		public async void ViewChanged()
		{
			var boards = await _jira.GetAllBoards();

			Boards = boards.Select(x => new NameValueModel
			{
				Name = x.Name,
				Value = x.Id.ToString()
			});
		}

		// Timer

		public string TimeElapsed
		{
			get { return _timeElapsed; }
			set
			{
				TimeSpan interval;
				if(!TimeSpan.TryParseExact(value, "c", null, out interval))
				{
					interval = new TimeSpan(0, 0, 0);
                }

				secondsElapsed = (int)interval.TotalSeconds;
				var text = interval.ToString();

				this.SetField(ref this._timeElapsed, text, () => this.TimeElapsed);
			}
		}

		public string Message
		{
			get { return _message; }
			set { this.SetField(ref this._message, value, () => this.Message); }
		}

		public DateTime SelectedDate
		{
			get { return _selectedDate; }
			set { this.SetField(ref this._selectedDate, value, () => this.SelectedDate); }
		}

		public DelegateCommand Start_Timer { get; private set; }

		public DelegateCommand Stop_Timer { get; private set; }

		public DelegateCommand Reset_Timer { get; private set; }

		public DelegateCommand LogWork { get; private set; }
	}
}
```